# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 12:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 547 windows, 15173 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1299 | 51.6 | 49.6 | $-162.13 | -1.2% | $837.87 | -0.5 | done | can't tell from luck |
| value_ev20 | 298 | 32.9 | 35.2 | $-362.88 | -12.2% | $637.12 | -1.6 | done | can't tell from luck |
| trend_filter | 884 | 50.8 | 50.9 | $-433.62 | -4.9% | $566.38 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1535 | 49.8 | 49.8 | $-697.25 | -4.5% | $302.75 | -1.8 | done | can't tell from luck |
| value_ev10 | 717 | 36.7 | 39.4 | $-820.87 | -11.4% | $179.13 | -2.6 | done | losing for real |
| value_ev5 | 1066 | 39.1 | 41.2 | $-1012.51 | -9.5% | $-12.51 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 1535 | 50.2 | 51.2 | $-1071.86 | -7.0% | $-71.86 | -2.8 | done | losing for real |
| coinflip | 2180 | 49.9 | 50.5 | $-1290.99 | -5.9% | $-290.99 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1299 | 48.4 | 51.2 | $-1378.92 | -10.6% | $-378.92 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2180 | 50.1 | 51.8 | $-1590.27 | -7.3% | $-590.27 | -3.6 | done | losing for real |
| always_up | 2180 | 46.7 | 50.0 | $-2487.29 | -11.4% | $-1487.29 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3435 | 47.4 | 49.2 | $-2870.45 |
| ETH | 3784 | 47.8 | 48.6 | $-2793.86 |
| SOL | 3960 | 47.6 | 48.7 | $-3095.71 |
| XRP | 3994 | 48.4 | 48.7 | $-2548.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
