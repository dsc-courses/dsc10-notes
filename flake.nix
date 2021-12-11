{
  description = "The build environment for the DSC 10 course notes.";

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

    in
      pkgs.mkShell {
        buildInputs = [
          pkgs.gnumake
          pkgs.poetry
        ];

        shellHook = ''
          poetry install
          export PATH=$(poetry env info -p)/bin:$PATH
          export PYTHONPATH=$(poetry env info -p)/lib/python3.8/site-packages:$PYTHONPATH
        '';

      }

    );

  };
}
