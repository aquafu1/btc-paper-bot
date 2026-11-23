# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1161 windows, 32094 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 618 | 34.8 | 35.3 | $-355.55 | -5.8% | $644.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1517 | 38.4 | 39.2 | $-822.32 | -5.4% | $177.68 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3220 | 50.7 | 50.4 | $-1097.50 | -3.4% | $-97.50 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2710 | 49.8 | 49.5 | $-1116.64 | -4.1% | $-116.64 | -2.1 | done | losing for real |
| value_ev5 | 2292 | 40.3 | 41.1 | $-1230.12 | -5.4% | $-230.12 | -2.2 | done | losing for real |
| trend_filter | 1899 | 49.1 | 50.5 | $-1472.25 | -7.8% | $-472.25 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2710 | 50.2 | 51.0 | $-1732.75 | -6.4% | $-732.75 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3220 | 49.3 | 50.2 | $-1886.57 | -5.9% | $-886.57 | -3.4 | done | losing for real |
| coinflip | 4636 | 50.2 | 50.2 | $-1948.48 | -4.2% | $-948.48 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4636 | 50.2 | 51.4 | $-2865.54 | -6.2% | $-1865.54 | -4.3 | done | losing for real |
| always_up | 4636 | 47.8 | 49.3 | $-3425.65 | -7.4% | $-2425.65 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7358 | 48.2 | 49.0 | $-3854.66 |
| ETH | 7956 | 48.2 | 48.4 | $-4594.95 |
| SOL | 8352 | 48.1 | 48.4 | $-4549.71 |
| XRP | 8428 | 48.1 | 48.2 | $-4954.06 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
