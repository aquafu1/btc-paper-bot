# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 683 windows, 18896 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 356 | 34.3 | 35.0 | $-234.96 | -6.6% | $765.04 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1599 | 50.3 | 49.5 | $-438.83 | -2.7% | $561.17 | -1.1 | done | can't tell from luck |
| value_ev10 | 872 | 38.4 | 39.2 | $-516.96 | -5.9% | $483.04 | -1.4 | done | can't tell from luck |
| trend_filter | 1099 | 50.3 | 50.9 | $-581.27 | -5.3% | $418.73 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1941 | 51.5 | 50.9 | $-603.13 | -3.1% | $396.87 | -1.4 | done | can't tell from luck |
| value_ev5 | 1311 | 40.7 | 41.2 | $-666.35 | -5.1% | $333.65 | -1.6 | done | can't tell from luck |
| coinflip | 2726 | 50.1 | 50.4 | $-1211.14 | -4.4% | $-211.14 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1599 | 49.7 | 51.4 | $-1238.41 | -7.7% | $-238.41 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1941 | 48.5 | 49.9 | $-1306.73 | -6.7% | $-306.73 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2726 | 50.8 | 51.8 | $-1456.84 | -5.3% | $-456.84 | -2.9 | done | losing for real |
| always_up | 2726 | 47.3 | 49.7 | $-2403.32 | -8.8% | $-1403.32 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4295 | 48.2 | 49.2 | $-2569.82 |
| ETH | 4704 | 48.3 | 48.6 | $-2803.93 |
| SOL | 4925 | 48.1 | 48.6 | $-2937.55 |
| XRP | 4972 | 48.5 | 48.4 | $-2346.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
