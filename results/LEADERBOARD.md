# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 683 windows, 18884 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 356 | 34.3 | 35.0 | $-234.96 | -6.6% | $765.04 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1599 | 50.3 | 49.5 | $-438.83 | -2.7% | $561.17 | -1.1 | done | can't tell from luck |
| value_ev10 | 872 | 38.4 | 39.2 | $-516.96 | -5.9% | $483.04 | -1.4 | done | can't tell from luck |
| trend_filter | 1098 | 50.4 | 50.9 | $-571.27 | -5.2% | $428.73 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1939 | 51.5 | 50.9 | $-616.06 | -3.2% | $383.94 | -1.4 | done | can't tell from luck |
| value_ev5 | 1310 | 40.6 | 41.1 | $-674.28 | -5.1% | $325.72 | -1.6 | done | can't tell from luck |
| coinflip | 2724 | 50.1 | 50.4 | $-1209.06 | -4.4% | $-209.06 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1599 | 49.7 | 51.4 | $-1238.41 | -7.7% | $-238.41 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1939 | 48.5 | 49.9 | $-1286.73 | -6.6% | $-286.73 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2724 | 50.9 | 51.8 | $-1436.84 | -5.3% | $-436.84 | -2.8 | done | losing for real |
| always_up | 2724 | 47.4 | 49.7 | $-2383.32 | -8.7% | $-1383.32 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4290 | 48.3 | 49.2 | $-2534.83 |
| ETH | 4704 | 48.3 | 48.6 | $-2803.93 |
| SOL | 4925 | 48.1 | 48.6 | $-2937.55 |
| XRP | 4965 | 48.5 | 48.4 | $-2330.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
