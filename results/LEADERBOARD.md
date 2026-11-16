# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 479 windows, 13146 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 239 | 35.1 | 35.9 | $-135.26 | -5.7% | $864.74 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1114 | 51.0 | 49.9 | $-236.56 | -2.1% | $763.44 | -0.7 | done | can't tell from luck |
| value_ev10 | 618 | 39.0 | 40.2 | $-384.93 | -6.2% | $615.07 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1328 | 50.1 | 50.0 | $-445.35 | -3.4% | $554.65 | -1.2 | done | can't tell from luck |
| trend_filter | 767 | 49.7 | 50.8 | $-469.83 | -6.1% | $530.17 | -1.7 | done | can't tell from luck |
| value_ev5 | 914 | 40.9 | 41.9 | $-537.62 | -5.9% | $462.38 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1328 | 49.9 | 51.5 | $-926.32 | -7.0% | $73.68 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1114 | 49.0 | 51.5 | $-999.39 | -9.0% | $0.61 | -3.1 | done | losing for real |
| coinflip | 1908 | 49.9 | 50.8 | $-1031.87 | -5.4% | $-31.87 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1908 | 49.7 | 51.7 | $-1391.15 | -7.3% | $-391.15 | -3.3 | done | losing for real |
| always_up | 1908 | 46.4 | 50.4 | $-2223.96 | -11.7% | $-1223.96 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2967 | 47.4 | 49.3 | $-2326.70 |
| ETH | 3295 | 48.1 | 48.9 | $-2185.97 |
| SOL | 3422 | 47.8 | 49.3 | $-2482.16 |
| XRP | 3462 | 48.6 | 49.1 | $-1787.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
