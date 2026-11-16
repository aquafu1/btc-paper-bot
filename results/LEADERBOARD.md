# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 562 windows, 15577 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1324 | 51.4 | 49.7 | $-226.30 | -1.7% | $773.70 | -0.6 | done | can't tell from luck |
| value_ev20 | 306 | 33.0 | 35.2 | $-355.92 | -11.6% | $644.08 | -1.6 | done | can't tell from luck |
| trend_filter | 902 | 50.7 | 51.1 | $-482.43 | -5.3% | $517.57 | -1.7 | done | can't tell from luck |
| value_ev10 | 740 | 37.6 | 39.4 | $-696.41 | -9.4% | $303.59 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1579 | 49.5 | 49.8 | $-789.74 | -5.0% | $210.26 | -2.0 | done | can't tell from luck |
| value_ev5 | 1100 | 39.7 | 41.2 | $-881.53 | -8.0% | $118.47 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1579 | 50.5 | 51.1 | $-972.02 | -6.2% | $27.98 | -2.5 | done | losing for real |
| coinflip | 2241 | 49.9 | 50.5 | $-1252.58 | -5.6% | $-252.58 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1324 | 48.6 | 51.2 | $-1322.83 | -10.0% | $-322.83 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2241 | 50.4 | 51.9 | $-1527.56 | -6.8% | $-527.56 | -3.4 | done | losing for real |
| always_up | 2241 | 47.3 | 49.9 | $-2205.56 | -9.8% | $-1205.56 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3528 | 47.6 | 49.2 | $-2716.15 |
| ETH | 3880 | 48.0 | 48.6 | $-2741.66 |
| SOL | 4066 | 47.9 | 48.7 | $-3000.02 |
| XRP | 4103 | 48.6 | 48.6 | $-2255.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
