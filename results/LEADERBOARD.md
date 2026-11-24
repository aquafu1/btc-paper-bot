# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 12:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1313 windows, 34880 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 687 | 34.2 | 35.3 | $-530.82 | -7.7% | $469.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1682 | 38.8 | 39.2 | $-775.92 | -4.6% | $224.08 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3497 | 50.8 | 50.2 | $-1032.48 | -3.0% | $-32.48 | -1.7 | done | can't tell from luck |
| value_ev5 | 2538 | 40.5 | 41.1 | $-1260.03 | -5.0% | $-260.03 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2929 | 49.5 | 49.4 | $-1353.59 | -4.6% | $-353.59 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2929 | 50.5 | 50.9 | $-1616.45 | -5.5% | $-616.45 | -3.1 | done | losing for real |
| trend_filter | 2073 | 48.9 | 50.5 | $-1712.39 | -8.3% | $-712.39 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3497 | 49.2 | 50.2 | $-2184.55 | -6.2% | $-1184.55 | -3.7 | done | losing for real |
| coinflip | 5016 | 49.9 | 50.0 | $-2326.18 | -4.6% | $-1326.18 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5016 | 50.4 | 51.4 | $-2928.92 | -5.8% | $-1928.92 | -4.3 | done | losing for real |
| always_up | 5016 | 47.9 | 49.3 | $-3595.83 | -7.2% | $-2595.83 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8455 | 47.9 | 48.8 | $-4972.23 |
| ETH | 9115 | 48.2 | 48.2 | $-4760.69 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
