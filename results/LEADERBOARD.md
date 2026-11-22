# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1101 windows, 30473 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 579 | 34.5 | 35.0 | $-341.49 | -5.9% | $658.51 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3077 | 51.1 | 50.4 | $-846.22 | -2.8% | $153.78 | -1.5 | done | can't tell from luck |
| value_ev10 | 1419 | 38.1 | 39.1 | $-871.09 | -6.1% | $128.91 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2590 | 49.6 | 49.4 | $-1139.63 | -4.4% | $-139.63 | -2.2 | done | losing for real |
| value_ev5 | 2151 | 40.0 | 41.0 | $-1250.70 | -5.8% | $-250.70 | -2.3 | done | losing for real |
| trend_filter | 1802 | 49.3 | 50.4 | $-1347.14 | -7.5% | $-347.14 | -3.2 | done | losing for real |
| reversal_60m_0.30pct | 2590 | 50.4 | 51.1 | $-1630.29 | -6.3% | $-630.29 | -3.3 | done | losing for real |
| coinflip | 4396 | 50.5 | 50.2 | $-1652.28 | -3.8% | $-652.28 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 3077 | 48.9 | 50.2 | $-2050.33 | -6.7% | $-1050.33 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4396 | 50.8 | 51.4 | $-2277.66 | -5.2% | $-1277.66 | -3.5 | done | losing for real |
| always_up | 4396 | 47.5 | 49.3 | $-3499.59 | -8.0% | $-2499.59 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6976 | 48.5 | 49.0 | $-3403.10 |
| ETH | 7546 | 48.2 | 48.4 | $-4455.61 |
| SOL | 7933 | 48.1 | 48.4 | $-4408.06 |
| XRP | 8018 | 48.2 | 48.2 | $-4639.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
