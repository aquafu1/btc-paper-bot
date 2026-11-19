# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 775 windows, 21367 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 403 | 33.0 | 34.9 | $-381.45 | -9.5% | $618.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2180 | 51.3 | 50.6 | $-615.22 | -2.8% | $384.78 | -1.3 | done | can't tell from luck |
| value_ev10 | 979 | 37.5 | 39.1 | $-744.62 | -7.6% | $255.38 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1807 | 49.8 | 49.6 | $-772.98 | -4.3% | $227.02 | -1.8 | done | can't tell from luck |
| trend_filter | 1255 | 49.8 | 50.8 | $-829.19 | -6.6% | $170.81 | -2.4 | done | losing for real |
| value_ev5 | 1480 | 39.8 | 41.0 | $-974.74 | -6.6% | $25.26 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1807 | 50.2 | 51.2 | $-1179.11 | -6.5% | $-179.11 | -2.8 | done | losing for real |
| coinflip | 3092 | 50.3 | 50.3 | $-1264.93 | -4.1% | $-264.93 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2180 | 48.7 | 50.2 | $-1487.01 | -6.8% | $-487.01 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3092 | 51.0 | 51.6 | $-1503.23 | -4.9% | $-503.23 | -2.8 | done | losing for real |
| always_up | 3092 | 47.0 | 49.5 | $-2858.57 | -9.2% | $-1858.57 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4851 | 48.2 | 49.1 | $-2950.28 |
| ETH | 5336 | 47.9 | 48.5 | $-3611.62 |
| SOL | 5562 | 48.0 | 48.5 | $-3280.40 |
| XRP | 5618 | 48.5 | 48.4 | $-2768.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
