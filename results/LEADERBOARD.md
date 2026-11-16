# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 531 windows, 14671 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1249 | 51.8 | 49.9 | $-44.22 | -0.4% | $955.78 | -0.1 | done | can't tell from luck |
| value_ev20 | 279 | 34.8 | 35.6 | $-202.64 | -7.3% | $797.36 | -0.9 | done | can't tell from luck |
| trend_filter | 860 | 50.0 | 50.8 | $-494.48 | -5.7% | $505.52 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1488 | 50.0 | 49.7 | $-527.72 | -3.5% | $472.28 | -1.4 | done | can't tell from luck |
| value_ev10 | 685 | 38.1 | 39.8 | $-549.21 | -8.0% | $450.79 | -1.7 | done | can't tell from luck |
| value_ev5 | 1022 | 40.2 | 41.5 | $-712.77 | -7.0% | $287.23 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1488 | 50.0 | 51.4 | $-1065.26 | -7.2% | $-65.26 | -2.8 | done | losing for real |
| coinflip | 2117 | 49.8 | 50.6 | $-1206.79 | -5.7% | $-206.79 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1249 | 48.2 | 51.2 | $-1293.22 | -10.4% | $-293.22 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2117 | 49.5 | 51.6 | $-1662.88 | -7.9% | $-662.88 | -3.8 | done | losing for real |
| always_up | 2117 | 46.7 | 50.2 | $-2351.59 | -11.1% | $-1351.59 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3331 | 47.5 | 49.3 | $-2636.32 |
| ETH | 3655 | 48.0 | 48.7 | $-2418.82 |
| SOL | 3824 | 47.6 | 48.9 | $-2837.57 |
| XRP | 3861 | 48.4 | 48.8 | $-2218.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
