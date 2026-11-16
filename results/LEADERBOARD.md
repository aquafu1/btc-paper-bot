# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 523 windows, 14417 settled trades, 73 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1228 | 51.4 | 49.8 | $-123.12 | -1.0% | $876.88 | -0.4 | done | can't tell from luck |
| value_ev20 | 269 | 34.6 | 35.6 | $-184.33 | -6.9% | $815.67 | -0.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1461 | 50.0 | 49.6 | $-483.74 | -3.3% | $516.26 | -1.3 | done | can't tell from luck |
| trend_filter | 847 | 49.7 | 50.7 | $-511.72 | -6.0% | $488.28 | -1.8 | done | can't tell from luck |
| value_ev10 | 671 | 38.0 | 39.7 | $-526.39 | -7.8% | $473.61 | -1.7 | done | can't tell from luck |
| value_ev5 | 1000 | 40.1 | 41.5 | $-690.00 | -6.9% | $310.00 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1461 | 50.0 | 51.6 | $-1069.76 | -7.3% | $-69.76 | -2.9 | done | losing for real |
| coinflip | 2084 | 50.0 | 50.7 | $-1115.59 | -5.4% | $-115.59 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1228 | 48.6 | 51.4 | $-1187.68 | -9.7% | $-187.68 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2084 | 49.5 | 51.6 | $-1601.30 | -7.7% | $-601.30 | -3.6 | done | losing for real |
| always_up | 2084 | 46.3 | 50.1 | $-2428.59 | -11.7% | $-1428.59 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3263 | 47.4 | 49.2 | $-2587.22 |
| ETH | 3596 | 48.0 | 48.7 | $-2352.64 |
| SOL | 3760 | 47.6 | 49.0 | $-2749.24 |
| XRP | 3798 | 48.3 | 48.8 | $-2233.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
