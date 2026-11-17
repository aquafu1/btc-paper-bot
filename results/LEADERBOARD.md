# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 609 windows, 16834 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1423 | 51.2 | 49.7 | $-195.78 | -1.4% | $804.22 | -0.5 | done | can't tell from luck |
| value_ev20 | 327 | 34.3 | 35.2 | $-244.70 | -7.5% | $755.30 | -1.0 | done | can't tell from luck |
| trend_filter | 971 | 50.4 | 51.0 | $-535.89 | -5.5% | $464.11 | -1.8 | done | can't tell from luck |
| value_ev10 | 784 | 38.3 | 39.4 | $-538.33 | -6.9% | $461.67 | -1.6 | done | can't tell from luck |
| value_ev5 | 1181 | 40.5 | 41.3 | $-692.71 | -5.9% | $307.29 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1719 | 50.7 | 50.9 | $-808.97 | -4.7% | $191.03 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1719 | 49.3 | 50.1 | $-939.67 | -5.5% | $60.33 | -2.3 | done | losing for real |
| coinflip | 2429 | 50.0 | 50.5 | $-1212.04 | -5.0% | $-212.04 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1423 | 48.8 | 51.3 | $-1344.62 | -9.4% | $-344.62 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2429 | 50.3 | 51.8 | $-1558.68 | -6.4% | $-558.68 | -3.3 | done | losing for real |
| always_up | 2429 | 47.1 | 49.8 | $-2302.27 | -9.5% | $-1302.27 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3826 | 48.0 | 49.2 | $-2513.19 |
| ETH | 4210 | 48.0 | 48.6 | $-2727.20 |
| SOL | 4371 | 47.9 | 48.8 | $-2875.92 |
| XRP | 4427 | 48.5 | 48.6 | $-2257.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
