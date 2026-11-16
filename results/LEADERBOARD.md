# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 12:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 545 windows, 15118 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1294 | 51.5 | 49.7 | $-192.00 | -1.5% | $808.00 | -0.5 | done | can't tell from luck |
| value_ev20 | 297 | 33.0 | 35.2 | $-352.88 | -11.9% | $647.12 | -1.6 | done | can't tell from luck |
| trend_filter | 881 | 50.7 | 50.9 | $-435.22 | -4.9% | $564.78 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1529 | 49.8 | 49.7 | $-668.85 | -4.4% | $331.15 | -1.7 | done | can't tell from luck |
| value_ev10 | 716 | 36.7 | 39.4 | $-810.87 | -11.3% | $189.13 | -2.5 | done | losing for real |
| value_ev5 | 1062 | 39.1 | 41.2 | $-1024.47 | -9.6% | $-24.47 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 1529 | 50.2 | 51.2 | $-1099.31 | -7.2% | $-99.31 | -2.9 | done | losing for real |
| coinflip | 2172 | 49.8 | 50.6 | $-1317.59 | -6.1% | $-317.59 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1294 | 48.5 | 51.2 | $-1343.50 | -10.4% | $-343.50 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2172 | 50.2 | 51.7 | $-1556.45 | -7.2% | $-556.45 | -3.5 | done | losing for real |
| always_up | 2172 | 46.7 | 50.0 | $-2469.32 | -11.4% | $-1469.32 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3427 | 47.5 | 49.2 | $-2832.28 |
| ETH | 3771 | 47.8 | 48.6 | $-2795.67 |
| SOL | 3945 | 47.6 | 48.7 | $-3153.52 |
| XRP | 3975 | 48.4 | 48.7 | $-2488.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
