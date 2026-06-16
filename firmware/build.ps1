param(
    [string]$Configuration = "Release",
    [switch]$RequireToolchain
)

$ErrorActionPreference = "Stop"

Write-Host "PlantSpeak firmware build contract"
Write-Host "Configuration: $Configuration"

$sdkPath = $env:DA14531_SDK_PATH
if ($RequireToolchain -and [string]::IsNullOrWhiteSpace($sdkPath)) {
    throw "DA14531_SDK_PATH is required when -RequireToolchain is set."
}

if ([string]::IsNullOrWhiteSpace($sdkPath)) {
    Write-Host "DA14531_SDK_PATH is not set; contract-only build evidence is active."
    exit 0
}

Write-Host "SDK path: $sdkPath"
Write-Host "TODO S5/S6: invoke project-specific DA14531 build command here."
exit 0
