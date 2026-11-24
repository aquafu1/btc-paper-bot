# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1293 windows, 34554 settled trades, 411 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 680 | 34.0 | 35.3 | $-551.91 | -8.1% | $448.09 | -1.6 | done | can't tell from luck |
| value_ev10 | 1664 | 38.7 | 39.2 | $-806.28 | -4.8% | $193.72 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3466 | 50.8 | 50.2 | $-1063.27 | -3.1% | $-63.27 | -1.8 | done | can't tell from luck |
| value_ev5 | 2512 | 40.4 | 41.1 | $-1283.97 | -5.1% | $-283.97 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2897 | 49.5 | 49.4 | $-1337.96 | -4.6% | $-337.96 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2897 | 50.5 | 51.0 | $-1632.35 | -5.6% | $-632.35 | -3.1 | done | losing for real |
| trend_filter | 2044 | 48.9 | 50.5 | $-1661.10 | -8.1% | $-661.10 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3466 | 49.2 | 50.3 | $-2171.20 | -6.3% | $-1171.20 | -3.7 | done | losing for real |
| coinflip | 4976 | 50.0 | 50.1 | $-2230.65 | -4.5% | $-1230.65 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4976 | 50.5 | 51.4 | $-2816.30 | -5.7% | $-1816.30 | -4.1 | done | losing for real |
| always_up | 4976 | 47.9 | 49.3 | $-3602.03 | -7.2% | $-2602.03 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8296 | 48.0 | 48.8 | $-4808.10 |
| ETH | 8948 | 48.2 | 48.2 | $-4764.67 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
