# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 973 windows, 26989 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2757 | 51.3 | 50.5 | $-722.36 | -2.6% | $277.64 | -1.4 | done | can't tell from luck |
| value_ev10 | 1231 | 37.9 | 39.1 | $-764.80 | -6.2% | $235.20 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2307 | 50.2 | 49.8 | $-870.93 | -3.8% | $129.07 | -1.8 | done | can't tell from luck |
| value_ev5 | 1867 | 39.8 | 41.0 | $-1118.05 | -6.0% | $-118.05 | -2.2 | done | losing for real |
| trend_filter | 1615 | 49.8 | 50.9 | $-1137.85 | -7.0% | $-137.85 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2307 | 49.8 | 50.9 | $-1674.46 | -7.3% | $-674.46 | -3.6 | done | losing for real |
| coinflip | 3884 | 50.2 | 50.3 | $-1810.32 | -4.7% | $-810.32 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2757 | 48.7 | 50.3 | $-1980.18 | -7.2% | $-980.18 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3884 | 50.7 | 51.6 | $-2149.68 | -5.5% | $-1149.68 | -3.6 | done | losing for real |
| always_up | 3884 | 46.8 | 49.6 | $-3874.60 | -10.0% | $-2874.60 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6150 | 48.1 | 49.1 | $-3566.01 |
| ETH | 6709 | 48.0 | 48.5 | $-4338.68 |
| SOL | 7047 | 48.2 | 48.6 | $-3985.54 |
| XRP | 7083 | 48.1 | 48.4 | $-4432.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
