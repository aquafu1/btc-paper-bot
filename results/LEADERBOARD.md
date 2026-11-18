# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 670 windows, 18523 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 347 | 34.3 | 35.2 | $-235.88 | -6.8% | $764.12 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1574 | 50.4 | 49.6 | $-422.17 | -2.7% | $577.83 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 1899 | 51.5 | 50.8 | $-551.33 | -2.9% | $448.67 | -1.3 | done | can't tell from luck |
| value_ev10 | 851 | 38.3 | 39.4 | $-561.27 | -6.6% | $438.73 | -1.6 | done | can't tell from luck |
| trend_filter | 1079 | 50.4 | 51.0 | $-563.95 | -5.2% | $436.05 | -1.8 | done | can't tell from luck |
| value_ev5 | 1284 | 40.7 | 41.3 | $-686.63 | -5.3% | $313.37 | -1.6 | done | can't tell from luck |
| coinflip | 2672 | 50.1 | 50.4 | $-1178.11 | -4.4% | $-178.11 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1574 | 49.6 | 51.3 | $-1235.54 | -7.8% | $-235.54 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1899 | 48.5 | 50.1 | $-1314.77 | -6.9% | $-314.77 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2672 | 50.8 | 51.8 | $-1441.82 | -5.4% | $-441.82 | -2.9 | done | losing for real |
| always_up | 2672 | 47.4 | 49.7 | $-2303.05 | -8.6% | $-1303.05 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4211 | 48.3 | 49.2 | $-2475.04 |
| ETH | 4617 | 48.2 | 48.6 | $-2797.47 |
| SOL | 4822 | 48.2 | 48.8 | $-2860.72 |
| XRP | 4873 | 48.5 | 48.5 | $-2361.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
