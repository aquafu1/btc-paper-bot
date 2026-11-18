# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 677 windows, 18737 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 350 | 34.9 | 35.1 | $-174.96 | -5.0% | $825.04 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1591 | 50.5 | 49.6 | $-374.53 | -2.4% | $625.47 | -0.9 | done | can't tell from luck |
| value_ev10 | 863 | 38.7 | 39.3 | $-455.56 | -5.3% | $544.44 | -1.3 | done | can't tell from luck |
| trend_filter | 1093 | 50.5 | 50.9 | $-536.97 | -4.9% | $463.03 | -1.7 | done | can't tell from luck |
| value_ev5 | 1301 | 40.8 | 41.3 | $-612.88 | -4.7% | $387.12 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1924 | 51.4 | 50.9 | $-634.48 | -3.3% | $365.52 | -1.5 | done | can't tell from luck |
| coinflip | 2700 | 50.1 | 50.4 | $-1177.38 | -4.4% | $-177.38 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1924 | 48.6 | 50.0 | $-1215.05 | -6.3% | $-215.05 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1591 | 49.5 | 51.3 | $-1266.70 | -8.0% | $-266.70 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2700 | 50.7 | 51.7 | $-1465.44 | -5.4% | $-465.44 | -2.9 | done | losing for real |
| always_up | 2700 | 47.3 | 49.7 | $-2360.92 | -8.7% | $-1360.92 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4263 | 48.3 | 49.2 | $-2438.16 |
| ETH | 4674 | 48.3 | 48.6 | $-2742.40 |
| SOL | 4877 | 48.2 | 48.7 | $-2761.78 |
| XRP | 4923 | 48.5 | 48.5 | $-2332.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
