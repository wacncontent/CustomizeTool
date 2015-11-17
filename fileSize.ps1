Param(
    [string]$file_name = "./output/newDocList/articles-.txt"
)

$file_list = (Get-Content $file_name).Split([char]0x000A);
$i=0;
foreach ($line in $file_list) {
    if ($line.StartsWith("articles") -Or $line.StartsWith("includes")) {
        $path = "./removeCommentOutput2/"+$line;
        $i+=(Get-Content $path | Measure-object -word).Words
    }
};
$i