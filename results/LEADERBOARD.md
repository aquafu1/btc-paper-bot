# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 5:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 615 windows, 16985 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1433 | 51.2 | 49.7 | $-213.52 | -1.5% | $786.48 | -0.6 | done | can't tell from luck |
| value_ev20 | 327 | 34.3 | 35.2 | $-244.70 | -7.5% | $755.30 | -1.0 | done | can't tell from luck |
| trend_filter | 980 | 50.3 | 51.0 | $-550.21 | -5.6% | $449.79 | -1.8 | done | can't tell from luck |
| value_ev10 | 790 | 38.1 | 39.4 | $-581.87 | -7.4% | $418.13 | -1.7 | done | can't tell from luck |
| value_ev5 | 1192 | 40.3 | 41.3 | $-764.88 | -6.4% | $235.12 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1737 | 50.7 | 50.9 | $-814.83 | -4.7% | $185.17 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1737 | 49.3 | 50.0 | $-955.97 | -5.5% | $44.03 | -2.3 | done | losing for real |
| coinflip | 2452 | 50.1 | 50.5 | $-1187.70 | -4.8% | $-187.70 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1433 | 48.8 | 51.3 | $-1336.34 | -9.3% | $-336.34 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2452 | 50.4 | 51.8 | $-1537.46 | -6.3% | $-537.46 | -3.2 | done | losing for real |
| always_up | 2452 | 47.1 | 49.8 | $-2299.32 | -9.4% | $-1299.32 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3860 | 48.1 | 49.2 | $-2533.18 |
| ETH | 4248 | 48.0 | 48.6 | $-2781.22 |
| SOL | 4410 | 48.0 | 48.8 | $-2875.36 |
| XRP | 4467 | 48.5 | 48.6 | $-2297.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
