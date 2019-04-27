
#Show list of PC's and the last time it was logged in/modified an it shows the DistinguishedName.The  Exports it to my .CSV File
Get-ADComputer -Filter * -properties *|select Name, DNSHostName, OperatingSystem, LastLogonDate,DistinguishedName| Export-CSV
ComputersinDomain.csv -NoTypeInformation -Encoding UTF8


#Shows when computers in domain where created .Then  Exports it to my .CSV File
Get-ADComputer -filter * -properties created | select-object name, created | sort created| Export-CSV
ComputersinDomain.csv -NoTypeInformation -Encoding UTF8


#Show if computers are active or inactive.Then  Exports it to my .CSV File
Get-ADComputer -filter * | Get-Service -ComputerName {$_.name} -DisplayName "Symantec Endpoint Protection"| Export-CSV
ComputersinDomain.csv -NoTypeInformation -Encoding UTF8