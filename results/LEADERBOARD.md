# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1228 windows, 33584 settled trades, 430 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 657 | 34.4 | 35.3 | $-467.83 | -7.1% | $532.17 | -1.4 | done | can't tell from luck |
| value_ev10 | 1607 | 38.7 | 39.2 | $-791.38 | -4.9% | $208.62 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3367 | 50.8 | 50.3 | $-1089.50 | -3.2% | $-89.50 | -1.9 | done | can't tell from luck |
| value_ev5 | 2427 | 40.5 | 41.1 | $-1226.61 | -5.1% | $-226.61 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2818 | 49.5 | 49.4 | $-1264.73 | -4.5% | $-264.73 | -2.4 | done | losing for real |
| trend_filter | 1985 | 48.8 | 50.4 | $-1665.10 | -8.4% | $-665.10 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2818 | 50.5 | 51.1 | $-1687.09 | -6.0% | $-687.09 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3367 | 49.2 | 50.2 | $-2078.26 | -6.2% | $-1078.26 | -3.6 | done | losing for real |
| coinflip | 4846 | 50.0 | 50.1 | $-2249.47 | -4.6% | $-1249.47 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4846 | 50.2 | 51.4 | $-2945.09 | -6.1% | $-1945.09 | -4.4 | done | losing for real |
| always_up | 4846 | 47.9 | 49.3 | $-3554.91 | -7.3% | $-2554.91 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7828 | 48.0 | 48.9 | $-4509.89 |
| ETH | 8446 | 48.1 | 48.3 | $-4925.85 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
