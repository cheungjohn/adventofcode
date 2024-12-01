module Day1 =
    open System.IO

    let GetLists () = 
        let filePath = Path.Combine(__SOURCE_DIRECTORY__, "Day1Input.txt")
        let Day1Text = System.IO.File.ReadAllLines(filePath)
        Day1Text
        |> Seq.map (fun line -> line.Split([| ' ' |], System.StringSplitOptions.RemoveEmptyEntries))
        |> Seq.filter (fun parts -> parts.Length >= 2)
        |> Seq.map (fun parts -> int parts.[0], int parts.[1])
        |> Seq.toList
        |> List.unzip
    let FindDistanceOfLists (leftList: List<int>, rightList: List<int>) =
        let leftListSorted = List.sort(leftList)
        let rightListSorted = List.sort(rightList)
        let distance = List.map2 (fun x y -> abs(x - y)) leftListSorted rightListSorted
        List.sum distance
    
    let FindSimilarityPoints (leftList: List<int>, rightList: List<int>) =
        let mutable points = 0
        let mutable rightHandList = rightList
        for i in leftList do
            let matches, rightHandList = List.partition ( fun x-> x = i ) rightHandList
            points <- points + (matches.Length * i)
        points

            

[<EntryPoint>]
let main args =
    let leftList, rightList = Day1.GetLists()
    let distance = Day1.FindDistanceOfLists(leftList,rightList)
    printfn "Total distance is: %d" distance
    let similarity = Day1.FindSimilarityPoints(leftList, rightList)
    printfn "Total similarity is: %d" similarity
    0
    