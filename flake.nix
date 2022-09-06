{
  description = "The build environment for the DSC 10 course notes.";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/22.05";
    nixpkgs-unstable.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs, nixpkgs-unstable }:
  let
    supportedSystems = [ "x86_64-linux" "x86_64-darwin" "aarch64-darwin"  ];
    forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);

  in
  {
    devShell = forAllSystems (system:
    let

      pkgs = import nixpkgs-unstable {
        inherit system;
      };

    in
      pkgs.mkShell {
        buildInputs = [
          pkgs.gnumake

          (
          pkgs.python310.withPackages(ps: with ps; [
            black
            matplotlib
            bokeh
            altair
            numpy
            pandas
            pyyaml
            notebook
            poetry
          ])
          )

        ];

        shellHook = ''
          poetry install
          export PATH=$(poetry env info -p)/bin:$PATH
          export PYTHONPATH=$(poetry env info -p)/lib/python3.8/site-packages:$PYTHONPATH
          export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [pkgs.stdenv.cc.cc]}
        '';

      }

    );

  };
}
