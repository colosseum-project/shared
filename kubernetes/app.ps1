[CmdletBinding()]
param (
    [Parameter()]
    [ValidateSet("apply", "create", "delete")]
    [string] $Action = "apply"
)

& kubectl.exe create namespace sandbox

Get-ChildItem -Path $PSScriptRoot\resources -File -Filter "*.yaml" | ForEach-Object -Process {
    & kubectl.exe $Action -f $_.FullName
}
