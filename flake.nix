{
  description = "The build environment for Dive Into Data Science";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/21.05";
  };

  outputs = { self, nixpkgs, }:
  let
    supportedSystems = [ "x86_64-linux" "x86_64-darwin" ];
    forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);

  in
  {
    devShell = forAllSystems (system:
    let
      pkgs = import nixpkgs {
        inherit system;
      };

      packageOverrides = pkgs.callPackage ./jupyterbook-requires.nix { };

      python = pkgs.python38.override { inherit packageOverrides; };

      jupyter-book = python.pkgs.buildPythonApplication rec {
        pname = "jupyter-book";
        version = "0.11.2";
        src = python.pkgs.fetchPypi {
          inherit pname version;
          sha256 = "sha256-4yKY4DwZ9RTHRQYokRQ2k8XgAaCYuunVnS5ENLIJnFQ=";
        };
        doCheck = false;
        buildInputs = [];
        checkInputs = [];
        nativeBuildInputs = [python.pkgs.ipykernel];
        propagatedBuildInputs = with python.pkgs; [
          click
          jsonschema
          jupyter-sphinx
          jupytext
          linkify-it-py
          myst-nb
          nbconvert
          sphinx-book-theme
          sphinx-comments
          sphinx-copybutton
          sphinx-external-toc
          sphinx-jupyterbook-latex
          sphinx-multitoc-numbering
          sphinx-panels
          sphinx-tabs
          sphinx-thebe
          sphinx-togglebutton
          sphinxcontrib-bibtex
          jupyter_client
        ];
      };

    babypandas = python.pkgs.buildPythonPackage {
      pname = "babypandas";
      version = "0.1.7";
      src = pkgs.fetchFromGitHub {
        owner = "eldridgejm";
        repo = "babypandas";
        rev = "a186aee54afb329cb4c5aa41d17e88986e9afa00";
        sha256 = "sha256-rTmcciCd6Yxl+LYjxFXmu+Sk3TDhFZfcGPYjOCVvt8Y=";
      };

      propagatedBuildInputs = [
        python.pkgs.pandas
        python.pkgs.numpy
      ];
    };

    in
      pkgs.mkShell {
        buildInputs = [
          pkgs.gnumake
          jupyter-book
          (
            python.withPackages (ps: [
              babypandas
              ps.jupyter
            ])
          )
        ];
      }
    );

  };
}
