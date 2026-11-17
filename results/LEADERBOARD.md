# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 599 windows, 16578 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 324 | 34.6 | 35.2 | $-214.70 | -6.6% | $785.30 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1403 | 51.0 | 49.6 | $-241.37 | -1.7% | $758.63 | -0.6 | done | can't tell from luck |
| value_ev10 | 777 | 38.2 | 39.4 | $-540.78 | -7.0% | $459.22 | -1.6 | done | can't tell from luck |
| trend_filter | 957 | 50.2 | 50.9 | $-556.54 | -5.8% | $443.46 | -1.8 | done | can't tell from luck |
| value_ev5 | 1165 | 40.5 | 41.2 | $-665.25 | -5.7% | $334.75 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1688 | 50.8 | 50.9 | $-799.34 | -4.7% | $200.66 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1688 | 49.2 | 50.0 | $-949.15 | -5.6% | $50.85 | -2.3 | done | losing for real |
| coinflip | 2391 | 50.0 | 50.5 | $-1195.47 | -5.0% | $-195.47 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1403 | 49.0 | 51.4 | $-1300.56 | -9.3% | $-300.56 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2391 | 50.3 | 51.7 | $-1527.21 | -6.4% | $-527.21 | -3.2 | done | losing for real |
| always_up | 2391 | 47.3 | 49.8 | $-2196.84 | -9.2% | $-1196.84 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3764 | 48.0 | 49.2 | $-2470.80 |
| ETH | 4136 | 48.0 | 48.6 | $-2661.13 |
| SOL | 4310 | 47.9 | 48.7 | $-2881.44 |
| XRP | 4368 | 48.6 | 48.6 | $-2173.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
