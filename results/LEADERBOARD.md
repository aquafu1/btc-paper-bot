# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 515 windows, 14207 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 266 | 34.2 | 35.5 | $-198.91 | -7.5% | $801.09 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1208 | 51.1 | 49.9 | $-221.13 | -1.8% | $778.88 | -0.6 | done | can't tell from luck |
| value_ev10 | 663 | 38.0 | 39.7 | $-513.23 | -7.7% | $486.77 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1442 | 49.7 | 49.6 | $-599.85 | -4.2% | $400.15 | -1.6 | done | can't tell from luck |
| trend_filter | 833 | 49.2 | 50.7 | $-613.24 | -7.4% | $386.76 | -2.2 | done | losing for real |
| value_ev5 | 986 | 39.9 | 41.5 | $-739.96 | -7.5% | $260.04 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 1442 | 50.3 | 51.6 | $-950.12 | -6.6% | $49.88 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1208 | 48.9 | 51.3 | $-1096.23 | -9.1% | $-96.23 | -3.2 | done | losing for real |
| coinflip | 2053 | 50.0 | 50.7 | $-1097.25 | -5.3% | $-97.25 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 2053 | 49.3 | 51.6 | $-1673.98 | -8.2% | $-673.98 | -3.8 | done | losing for real |
| always_up | 2053 | 46.4 | 50.1 | $-2351.10 | -11.5% | $-1351.10 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3225 | 47.2 | 49.2 | $-2692.52 |
| ETH | 3546 | 48.0 | 48.7 | $-2368.22 |
| SOL | 3698 | 47.6 | 49.0 | $-2790.01 |
| XRP | 3738 | 48.3 | 48.8 | $-2204.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
