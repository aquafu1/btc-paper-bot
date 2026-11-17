# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 638 windows, 17657 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1494 | 51.1 | 49.6 | $-207.32 | -1.4% | $792.68 | -0.5 | done | can't tell from luck |
| value_ev20 | 333 | 34.2 | 35.3 | $-246.80 | -7.4% | $753.20 | -1.0 | done | can't tell from luck |
| trend_filter | 1020 | 50.5 | 50.8 | $-507.93 | -5.0% | $492.07 | -1.6 | done | can't tell from luck |
| value_ev10 | 812 | 38.4 | 39.5 | $-551.51 | -6.8% | $448.49 | -1.6 | done | can't tell from luck |
| value_ev5 | 1232 | 40.8 | 41.4 | $-660.01 | -5.4% | $339.99 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1817 | 51.1 | 51.0 | $-723.34 | -4.0% | $276.66 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1817 | 48.9 | 50.0 | $-1090.98 | -6.0% | $-90.98 | -2.6 | done | losing for real |
| coinflip | 2546 | 50.1 | 50.5 | $-1175.48 | -4.6% | $-175.48 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 2546 | 50.7 | 51.7 | $-1359.63 | -5.3% | $-359.63 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1494 | 48.9 | 51.4 | $-1368.94 | -9.2% | $-368.94 | -3.6 | done | losing for real |
| always_up | 2546 | 47.3 | 49.7 | $-2226.29 | -8.7% | $-1226.29 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4016 | 48.4 | 49.3 | $-2345.13 |
| ETH | 4420 | 48.3 | 48.6 | $-2601.36 |
| SOL | 4579 | 48.0 | 48.8 | $-2923.57 |
| XRP | 4642 | 48.5 | 48.5 | $-2248.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
