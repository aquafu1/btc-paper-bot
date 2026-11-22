# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 5:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1093 windows, 30244 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 570 | 34.6 | 35.0 | $-327.96 | -5.8% | $672.04 | -1.0 | done | can't tell from luck |
| value_ev10 | 1400 | 38.0 | 39.1 | $-873.63 | -6.2% | $126.37 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3055 | 51.1 | 50.5 | $-895.81 | -2.9% | $104.19 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2574 | 49.7 | 49.4 | $-1094.77 | -4.3% | $-94.77 | -2.1 | done | losing for real |
| value_ev5 | 2128 | 40.0 | 41.0 | $-1234.41 | -5.8% | $-234.41 | -2.3 | done | losing for real |
| trend_filter | 1796 | 49.4 | 50.4 | $-1301.80 | -7.2% | $-301.80 | -3.1 | done | losing for real |
| coinflip | 4364 | 50.6 | 50.2 | $-1593.13 | -3.7% | $-593.13 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2574 | 50.3 | 51.1 | $-1668.25 | -6.5% | $-668.25 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3055 | 48.9 | 50.2 | $-1997.75 | -6.5% | $-997.75 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4364 | 50.8 | 51.4 | $-2188.46 | -5.0% | $-1188.46 | -3.4 | done | losing for real |
| always_up | 4364 | 47.5 | 49.3 | $-3538.72 | -8.1% | $-2538.72 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6913 | 48.5 | 49.0 | $-3389.42 |
| ETH | 7493 | 48.2 | 48.4 | $-4392.42 |
| SOL | 7882 | 48.1 | 48.4 | $-4431.30 |
| XRP | 7956 | 48.3 | 48.2 | $-4501.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
