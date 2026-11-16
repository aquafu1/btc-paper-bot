# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 483 windows, 13258 settled trades, 78 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 241 | 35.3 | 35.9 | $-112.29 | -4.7% | $887.71 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1125 | 51.0 | 49.8 | $-173.09 | -1.5% | $826.91 | -0.5 | done | can't tell from luck |
| value_ev10 | 622 | 39.2 | 40.1 | $-323.65 | -5.2% | $676.35 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 1339 | 50.3 | 50.0 | $-386.29 | -2.9% | $613.71 | -1.1 | done | can't tell from luck |
| value_ev5 | 920 | 41.2 | 41.8 | $-439.82 | -4.8% | $560.18 | -1.2 | done | can't tell from luck |
| trend_filter | 775 | 49.5 | 50.8 | $-493.93 | -6.4% | $506.07 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1339 | 49.7 | 51.5 | $-980.47 | -7.3% | $19.53 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1125 | 49.0 | 51.5 | $-1016.00 | -9.0% | $-16.00 | -3.1 | done | losing for real |
| coinflip | 1924 | 49.9 | 50.8 | $-1022.65 | -5.3% | $-22.65 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1924 | 49.6 | 51.7 | $-1417.24 | -7.4% | $-417.24 | -3.4 | done | losing for real |
| always_up | 1924 | 46.5 | 50.5 | $-2213.30 | -11.5% | $-1213.30 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2991 | 47.4 | 49.3 | $-2327.15 |
| ETH | 3323 | 48.2 | 48.9 | $-2061.68 |
| SOL | 3452 | 47.8 | 49.3 | $-2434.00 |
| XRP | 3492 | 48.5 | 49.1 | $-1755.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
