[CmdletBinding()]
param (
    [Parameter()]
    [ValidateSet("create", "delete")]
    [string] $Action = "create"
)

switch ($Action) {
    "create" { & kind.exe create cluster --config .\kind_config.yaml }
    "delete" { & kind.exe delete clusters colosseum-project }
}
