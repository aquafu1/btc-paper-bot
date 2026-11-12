# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 5:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 144 windows, 3610 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 247 | 61.9 | 53.2 | $+342.92 | +13.9% | $1342.92 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 348 | 57.2 | 52.3 | $+236.43 | +6.8% | $1236.43 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 568 | 52.1 | 51.3 | $-155.21 | -2.7% | $844.79 | -0.7 | done | can't tell from luck |
| value_ev20 | 70 | 30.0 | 36.9 | $-165.47 | -23.6% | $834.53 | -1.6 | Sun 4:00 AM | too few trades (70/200) |
| coinflip | 568 | 51.6 | 50.9 | $-199.52 | -3.5% | $800.48 | -0.9 | done | can't tell from luck |
| value_ev10 | 190 | 36.3 | 40.6 | $-285.28 | -15.0% | $714.72 | -1.8 | Thu 7:15 AM | too few trades (190/200) |
| trend_filter | 181 | 39.8 | 49.1 | $-398.37 | -22.0% | $601.63 | -3.0 | Thu 9:15 AM | too few trades (181/200) |
| value_ev5 | 275 | 37.5 | 42.2 | $-424.16 | -15.4% | $575.84 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 348 | 42.8 | 50.0 | $-606.05 | -17.4% | $393.95 | -3.3 | done | losing for real |
| momentum_60m_0.30pct | 247 | 38.1 | 49.1 | $-615.20 | -24.9% | $384.80 | -4.0 | done | losing for real |
| always_up | 568 | 46.8 | 50.0 | $-620.96 | -10.9% | $379.04 | -2.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 771 | 45.5 | 49.5 | $-849.52 |
| ETH | 892 | 45.0 | 48.7 | $-1076.21 |
| SOL | 954 | 48.4 | 48.8 | $-674.00 |
| XRP | 993 | 50.5 | 49.1 | $-291.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
