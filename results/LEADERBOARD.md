# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1134 windows, 31352 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 601 | 34.6 | 35.2 | $-363.62 | -6.1% | $636.38 | -1.1 | done | can't tell from luck |
| value_ev10 | 1469 | 38.2 | 39.2 | $-890.10 | -6.1% | $109.90 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3156 | 51.0 | 50.5 | $-925.65 | -2.9% | $74.35 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2646 | 49.7 | 49.4 | $-1119.05 | -4.2% | $-119.05 | -2.2 | done | losing for real |
| value_ev5 | 2223 | 40.1 | 41.1 | $-1282.03 | -5.8% | $-282.03 | -2.3 | done | losing for real |
| trend_filter | 1859 | 49.1 | 50.4 | $-1429.34 | -7.7% | $-429.34 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2646 | 50.3 | 51.1 | $-1677.08 | -6.3% | $-677.08 | -3.3 | done | losing for real |
| coinflip | 4532 | 50.3 | 50.2 | $-1841.36 | -4.1% | $-841.36 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3156 | 49.0 | 50.2 | $-2001.69 | -6.3% | $-1001.69 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4532 | 50.3 | 51.4 | $-2769.37 | -6.1% | $-1769.37 | -4.2 | done | losing for real |
| always_up | 4532 | 47.8 | 49.3 | $-3363.05 | -7.4% | $-2363.05 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7184 | 48.4 | 49.0 | $-3633.34 |
| ETH | 7771 | 48.2 | 48.4 | $-4548.76 |
| SOL | 8158 | 48.0 | 48.4 | $-4656.70 |
| XRP | 8239 | 48.1 | 48.2 | $-4823.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
