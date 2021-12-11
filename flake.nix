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
      version = "0.1.6";
      src = pkgs.fetchFromGitHub {
        owner = "babypandas-dev";
        repo = "babypandas";
        rev = "dc51b243cda75b85a7e8bbe6ce2a5412d895755a";
        sha256 = "sha256-37TvMfGX2CmwA3b/9tb28lkBVNjkrjwHCJEOlSYKrkI=";
      };

      nativeBuildInputs = with pkgs.python38Packages; [ pytest pytestrunner ];
      propagatedBuildInputs = with pkgs.python38Packages; [ pandas ];
      doCheck = false;

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

        # this is used on macOS to ensure that send2trash will function without an error
        # if not provided, you'll see the following error when starting jupyter:
        # AttributeError: dlsym(RTLD_DEFAULT, GetMacOSStatusCommentString): symbol not found
        shellHook = ''
          export DYLD_LIBRARY_PATH=/System/Library/Frameworks/Foundation.framework/Versions/C/Resources/BridgeSupport
        '';
      }
    );

  };
}
