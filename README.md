Silahlar means Weapons in turkish, the website may be turkish. Sorry about that. But i added the Python file too. You can download this html page and run python code.
https://fortnite.gg/weapons

This code totally written by Cursor AI.

example verse code


using { /UnrealEngine.com }

    #You must give the json text as string, in the details panel of device.
    @editable JsonFile : string = ""

    OnBegin<override>()<suspends>:void=
        if (ParsedResult : JSON.value = JSON.Parse[JsonFile], ResultArray : []JSON.value = ParsedResult.AsArray[])
        {
            for (Result : ResultArray, JsonObject : [string]JSON.value = Result.AsObject[])
            {
                if (Index : int = JsonObject["index"].AsInt[])
                {
                    Print("{Index}")
                }
            }
        }
            
