# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 1:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 454 windows, 12449 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 227 | 34.8 | 36.0 | $-152.39 | -6.7% | $847.61 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1055 | 51.2 | 50.1 | $-210.74 | -2.0% | $789.26 | -0.7 | done | can't tell from luck |
| trend_filter | 718 | 50.0 | 50.7 | $-389.13 | -5.4% | $610.87 | -1.5 | done | can't tell from luck |
| value_ev10 | 585 | 38.8 | 40.1 | $-391.01 | -6.7% | $608.99 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1259 | 49.9 | 50.0 | $-490.59 | -3.9% | $509.41 | -1.4 | done | can't tell from luck |
| value_ev5 | 867 | 40.9 | 41.9 | $-505.69 | -5.8% | $494.31 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1259 | 50.1 | 51.6 | $-902.72 | -7.2% | $97.28 | -2.7 | done | losing for real |
| coinflip | 1808 | 49.8 | 50.8 | $-1025.70 | -5.7% | $-25.70 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1055 | 48.8 | 51.7 | $-1043.16 | -9.9% | $-43.16 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1808 | 49.6 | 51.5 | $-1325.68 | -7.3% | $-325.68 | -3.2 | done | losing for real |
| always_up | 1808 | 46.1 | 50.6 | $-2291.80 | -12.7% | $-1291.80 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2811 | 47.5 | 49.3 | $-2247.73 |
| ETH | 3125 | 47.9 | 48.8 | $-2077.99 |
| SOL | 3241 | 47.7 | 49.3 | $-2526.44 |
| XRP | 3272 | 48.5 | 49.2 | $-1876.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
