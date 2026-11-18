# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 749 windows, 20693 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 391 | 33.5 | 34.9 | $-321.39 | -8.2% | $678.61 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2116 | 51.5 | 50.6 | $-501.19 | -2.4% | $498.81 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1750 | 50.0 | 49.6 | $-655.37 | -3.7% | $344.63 | -1.6 | done | can't tell from luck |
| value_ev10 | 948 | 37.8 | 39.1 | $-659.74 | -7.0% | $340.26 | -1.7 | done | can't tell from luck |
| trend_filter | 1220 | 49.8 | 50.9 | $-822.88 | -6.7% | $177.12 | -2.4 | done | losing for real |
| value_ev5 | 1429 | 40.2 | 41.1 | $-842.97 | -5.9% | $157.03 | -1.9 | done | can't tell from luck |
| coinflip | 2991 | 50.4 | 50.3 | $-1159.25 | -3.9% | $-159.25 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1750 | 50.0 | 51.2 | $-1215.28 | -6.9% | $-215.28 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2116 | 48.5 | 50.2 | $-1549.06 | -7.3% | $-549.06 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2991 | 50.7 | 51.8 | $-1714.32 | -5.7% | $-714.32 | -3.2 | done | losing for real |
| always_up | 2991 | 47.0 | 49.6 | $-2796.09 | -9.3% | $-1796.09 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4681 | 48.1 | 49.1 | $-3009.08 |
| ETH | 5158 | 48.0 | 48.5 | $-3357.29 |
| SOL | 5397 | 48.0 | 48.6 | $-3221.46 |
| XRP | 5457 | 48.5 | 48.5 | $-2649.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
