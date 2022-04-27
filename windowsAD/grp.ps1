Import-Module ActiveDirectory
$groups = Import-Csv 'c:\ft\grp.csv'
#$SEED = 'AAAA50123456789012345678901234567890123456789512345678961234'
$SEED = 'ABAA50123456789012345678901234567890123456789512345678961234'
#$SEED = 'BBB950123456789012345678901234567890123456789512345678961234'
foreach ($group in $groups) {
#New-ADGroup -Name agp$group.name -Path ?CN=Domain Users,CN=Users,DC=smb2016,DC=local? -Description ?Bulk? -GroupCategory Security -GroupScope Universal -Managedby BC
$gName  = $SEED + $group.name 
Get-ADGroup "Domain Users" -Properties Description | New-ADGroup -Name $gName  -SamAccountName $gName  -GroupCategory Distribution -PassThru

}
