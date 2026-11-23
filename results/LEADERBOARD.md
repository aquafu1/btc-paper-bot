# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1212 windows, 33342 settled trades, 272 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1595 | 38.7 | 39.2 | $-771.50 | -4.8% | $228.50 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3341 | 50.8 | 50.3 | $-1096.00 | -3.3% | $-96.00 | -1.9 | done | can't tell from luck |
| value_ev5 | 2411 | 40.5 | 41.1 | $-1189.84 | -4.9% | $-189.84 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2795 | 49.5 | 49.4 | $-1272.88 | -4.6% | $-272.88 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2795 | 50.5 | 51.1 | $-1661.55 | -5.9% | $-661.55 | -3.2 | done | losing for real |
| trend_filter | 1970 | 48.7 | 50.4 | $-1662.81 | -8.4% | $-662.81 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3341 | 49.2 | 50.2 | $-2043.21 | -6.1% | $-1043.21 | -3.6 | done | losing for real |
| coinflip | 4814 | 50.0 | 50.1 | $-2188.13 | -4.5% | $-1188.13 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4814 | 50.3 | 51.4 | $-2896.16 | -6.0% | $-1896.16 | -4.3 | done | losing for real |
| always_up | 4814 | 47.9 | 49.3 | $-3511.07 | -7.3% | $-2511.07 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7705 | 48.1 | 48.9 | $-4269.88 |
| ETH | 8327 | 48.1 | 48.3 | $-4882.48 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
