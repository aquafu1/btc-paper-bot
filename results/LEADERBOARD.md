# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 5:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1045 windows, 28998 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 541 | 34.6 | 35.1 | $-305.47 | -5.6% | $694.53 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2943 | 51.2 | 50.5 | $-787.53 | -2.7% | $212.47 | -1.5 | done | can't tell from luck |
| value_ev10 | 1341 | 37.4 | 39.2 | $-1016.04 | -7.6% | $-16.04 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2476 | 49.7 | 49.6 | $-1146.03 | -4.6% | $-146.03 | -2.3 | done | losing for real |
| trend_filter | 1732 | 49.3 | 50.7 | $-1343.79 | -7.8% | $-343.79 | -3.3 | done | losing for real |
| value_ev5 | 2030 | 39.4 | 41.0 | $-1441.77 | -7.1% | $-441.77 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2476 | 50.3 | 51.0 | $-1591.47 | -6.4% | $-591.47 | -3.3 | done | losing for real |
| coinflip | 4172 | 50.5 | 50.3 | $-1666.81 | -4.0% | $-666.81 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2943 | 48.8 | 50.3 | $-2059.68 | -7.0% | $-1059.68 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4172 | 50.8 | 51.5 | $-2252.63 | -5.4% | $-1252.63 | -3.6 | done | losing for real |
| always_up | 4172 | 47.3 | 49.4 | $-3671.35 | -8.8% | $-2671.35 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6610 | 48.3 | 49.0 | $-3533.42 |
| ETH | 7183 | 48.1 | 48.5 | $-4477.12 |
| SOL | 7573 | 48.1 | 48.5 | $-4505.32 |
| XRP | 7632 | 48.1 | 48.3 | $-4766.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
