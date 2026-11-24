# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1257 windows, 34011 settled trades, 410 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1628 | 38.4 | 39.2 | $-920.17 | -5.7% | $79.83 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3410 | 50.7 | 50.3 | $-1147.75 | -3.4% | $-147.75 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2854 | 49.6 | 49.4 | $-1271.93 | -4.5% | $-271.93 | -2.4 | done | losing for real |
| value_ev5 | 2461 | 40.3 | 41.1 | $-1369.62 | -5.6% | $-369.62 | -2.3 | done | losing for real |
| trend_filter | 2014 | 48.9 | 50.4 | $-1640.07 | -8.1% | $-640.07 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2854 | 50.4 | 51.1 | $-1721.69 | -6.0% | $-721.69 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3410 | 49.3 | 50.2 | $-2072.21 | -6.1% | $-1072.21 | -3.6 | done | losing for real |
| coinflip | 4905 | 50.1 | 50.1 | $-2190.23 | -4.5% | $-1190.23 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4905 | 50.4 | 51.4 | $-2878.74 | -5.9% | $-1878.74 | -4.2 | done | losing for real |
| always_up | 4905 | 47.8 | 49.4 | $-3641.49 | -7.4% | $-2641.49 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8036 | 48.0 | 48.9 | $-4703.46 |
| ETH | 8665 | 48.1 | 48.3 | $-5090.36 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
