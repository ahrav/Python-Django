public int MakeChange(int[] coins, int change){
    int[] minCoins = new int[change]
    for (int i = 0; i < change.length; i++)
    {
        int coinCount = change[i];
        foreach (var coin in coins)
        {
            if (coin <= change[i])
            {
                if (minCoins[change[i] - j] + 1 < coinCount)
                {
                    coinCount = minCoins[change[i] -j] + 1;
                }
            }
        }
        minCoins[change[i]] = coinCount;
    }
    return minCoins[change];
}

System.Console.WriteLine(MakeChange(new int[]{1, 5, 10, 25}), 32);