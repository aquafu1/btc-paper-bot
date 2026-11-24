# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1324 windows, 35039 settled trades, 417 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 689 | 34.4 | 35.3 | $-497.07 | -7.2% | $502.93 | -1.4 | done | can't tell from luck |
| value_ev10 | 1689 | 38.8 | 39.2 | $-769.05 | -4.6% | $230.95 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3511 | 50.9 | 50.2 | $-1023.79 | -2.9% | $-23.79 | -1.7 | done | can't tell from luck |
| value_ev5 | 2548 | 40.5 | 41.1 | $-1238.95 | -4.9% | $-238.95 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2945 | 49.4 | 49.4 | $-1418.70 | -4.8% | $-418.70 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2945 | 50.6 | 50.9 | $-1560.07 | -5.3% | $-560.07 | -2.9 | done | losing for real |
| trend_filter | 2087 | 48.7 | 50.5 | $-1793.38 | -8.6% | $-793.38 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3511 | 49.1 | 50.2 | $-2201.57 | -6.3% | $-1201.57 | -3.8 | done | losing for real |
| coinflip | 5038 | 49.9 | 50.0 | $-2349.79 | -4.7% | $-1349.79 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5038 | 50.3 | 51.4 | $-3033.33 | -6.0% | $-2033.33 | -4.4 | done | losing for real |
| always_up | 5038 | 47.8 | 49.3 | $-3702.90 | -7.3% | $-2702.90 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8533 | 47.9 | 48.8 | $-5135.76 |
| ETH | 9196 | 48.2 | 48.2 | $-4868.61 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
