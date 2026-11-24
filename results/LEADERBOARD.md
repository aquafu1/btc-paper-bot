# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 2:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1272 windows, 34226 settled trades, 405 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 668 | 34.1 | 35.3 | $-521.06 | -7.8% | $478.94 | -1.5 | done | can't tell from luck |
| value_ev10 | 1642 | 38.6 | 39.2 | $-834.47 | -5.1% | $165.53 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3430 | 50.6 | 50.2 | $-1212.97 | -3.5% | $-212.97 | -2.1 | done | losing for real |
| value_ev5 | 2482 | 40.5 | 41.1 | $-1277.44 | -5.1% | $-277.44 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2872 | 49.5 | 49.4 | $-1318.28 | -4.6% | $-318.28 | -2.5 | done | losing for real |
| trend_filter | 2028 | 49.0 | 50.4 | $-1617.01 | -8.0% | $-617.01 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2872 | 50.5 | 51.0 | $-1660.57 | -5.8% | $-660.57 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3430 | 49.4 | 50.2 | $-2014.89 | -5.9% | $-1014.89 | -3.5 | done | losing for real |
| coinflip | 4934 | 50.0 | 50.1 | $-2243.88 | -4.5% | $-1243.88 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4934 | 50.5 | 51.4 | $-2772.26 | -5.6% | $-1772.26 | -4.1 | done | losing for real |
| always_up | 4934 | 47.9 | 49.4 | $-3605.51 | -7.3% | $-2605.51 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8133 | 48.0 | 48.9 | $-4740.07 |
| ETH | 8783 | 48.2 | 48.3 | $-4754.02 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
