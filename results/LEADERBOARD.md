# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 4:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1618 windows, 38973 settled trades, 344 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 824 | 34.2 | 35.2 | $-651.33 | -7.9% | $348.67 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3842 | 50.9 | 50.0 | $-1005.24 | -2.6% | $-5.24 | -1.6 | done | can't tell from luck |
| value_ev10 | 1951 | 38.3 | 39.0 | $-1124.66 | -5.8% | $-124.66 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3215 | 51.1 | 50.9 | $-1460.99 | -4.5% | $-460.99 | -2.6 | done | losing for real |
| value_ev5 | 2918 | 40.3 | 41.0 | $-1564.04 | -5.4% | $-564.04 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3215 | 48.9 | 49.2 | $-1760.52 | -5.5% | $-760.52 | -3.1 | done | losing for real |
| trend_filter | 2285 | 48.5 | 50.4 | $-2038.85 | -8.9% | $-1038.85 | -4.4 | done | losing for real |
| coinflip | 5627 | 50.1 | 49.9 | $-2326.50 | -4.1% | $-1326.50 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3842 | 49.1 | 50.2 | $-2376.65 | -6.2% | $-1376.65 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5627 | 50.2 | 51.3 | $-3464.00 | -6.2% | $-2464.00 | -4.8 | done | losing for real |
| always_up | 5627 | 48.1 | 49.1 | $-3668.55 | -6.5% | $-2668.55 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10399 | 47.9 | 48.6 | $-5928.28 |
| ETH | 11264 | 47.9 | 47.7 | $-5928.82 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
