# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 768 windows, 21178 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 401 | 33.2 | 34.9 | $-361.45 | -9.0% | $638.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2163 | 51.5 | 50.6 | $-522.29 | -2.4% | $477.71 | -1.1 | done | can't tell from luck |
| value_ev10 | 971 | 37.7 | 39.1 | $-691.05 | -7.1% | $308.95 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1788 | 49.8 | 49.5 | $-732.11 | -4.1% | $267.89 | -1.7 | done | can't tell from luck |
| trend_filter | 1247 | 49.6 | 50.8 | $-855.43 | -6.9% | $144.57 | -2.5 | done | losing for real |
| value_ev5 | 1465 | 40.0 | 41.0 | $-907.45 | -6.2% | $92.55 | -2.0 | done | losing for real |
| coinflip | 3064 | 50.4 | 50.2 | $-1194.37 | -3.9% | $-194.37 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1788 | 50.2 | 51.3 | $-1218.36 | -6.8% | $-218.36 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2163 | 48.5 | 50.2 | $-1586.95 | -7.3% | $-586.95 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3064 | 50.8 | 51.7 | $-1619.19 | -5.3% | $-619.19 | -3.0 | done | losing for real |
| always_up | 3064 | 47.1 | 49.6 | $-2832.49 | -9.2% | $-1832.49 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4804 | 48.2 | 49.1 | $-2939.94 |
| ETH | 5286 | 48.0 | 48.5 | $-3554.05 |
| SOL | 5513 | 48.0 | 48.6 | $-3320.81 |
| XRP | 5575 | 48.5 | 48.4 | $-2706.34 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
