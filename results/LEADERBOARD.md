# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 678 windows, 18756 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 350 | 34.9 | 35.1 | $-174.96 | -5.0% | $825.04 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1592 | 50.6 | 49.6 | $-368.83 | -2.3% | $631.17 | -0.9 | done | can't tell from luck |
| value_ev10 | 863 | 38.7 | 39.3 | $-455.56 | -5.3% | $544.44 | -1.3 | done | can't tell from luck |
| trend_filter | 1094 | 50.5 | 50.9 | $-531.27 | -4.9% | $468.73 | -1.6 | done | can't tell from luck |
| value_ev5 | 1301 | 40.8 | 41.3 | $-612.88 | -4.7% | $387.12 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1926 | 51.3 | 50.9 | $-654.48 | -3.4% | $345.52 | -1.5 | done | can't tell from luck |
| coinflip | 2704 | 50.1 | 50.4 | $-1185.97 | -4.4% | $-185.97 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1926 | 48.7 | 50.0 | $-1203.89 | -6.3% | $-203.89 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1592 | 49.4 | 51.3 | $-1276.70 | -8.0% | $-276.70 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2704 | 50.8 | 51.8 | $-1441.03 | -5.3% | $-441.03 | -2.9 | done | losing for real |
| always_up | 2704 | 47.4 | 49.7 | $-2336.50 | -8.6% | $-1336.50 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4266 | 48.4 | 49.2 | $-2420.33 |
| ETH | 4677 | 48.3 | 48.6 | $-2737.78 |
| SOL | 4885 | 48.2 | 48.7 | $-2763.28 |
| XRP | 4928 | 48.5 | 48.5 | $-2320.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
