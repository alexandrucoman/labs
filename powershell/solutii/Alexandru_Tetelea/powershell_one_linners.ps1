# Top 5 procese care consuma procesorul
function topProcesses {
   echo (Get-Process | Sort-Object CPU -desc | Select-Object -first 5)
}

# Adresele ipv4
function ipAdresses {
    $AllInterfaces = Get-NetIPAddress
    echo ($AllInterfaces.IPAddress -match "^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")
    
}

# Enumeram folderurile si subfolderurile
function enumFolders {
    $a = Get-ChildItem -Recurse | ?{ $_.PSIsContainer }
    echo $a.Count
}

# All TXT files
function listTXTfiles {
    Echo (Get-ChildItem -Recurse -Filter "*.txt" | select FullName)
    
}

# Size of all files in folders and subfolders
function filesSize {
     $sum=0
     Get-ChildItem -Recurse -Filter "*.txt" | ForEach-Object {$sum+=$_.Length}
     echo $sum
    
}
topProcesses
ipAdresses
enumFolders
sumElements