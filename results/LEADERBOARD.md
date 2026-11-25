# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1415 windows, 36311 settled trades, 457 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 728 | 34.9 | 35.3 | $-445.63 | -6.1% | $554.37 | -1.3 | done | can't tell from luck |
| value_ev10 | 1759 | 39.0 | 39.2 | $-705.98 | -4.0% | $294.02 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3628 | 50.8 | 50.1 | $-1044.85 | -2.9% | $-44.85 | -1.7 | done | can't tell from luck |
| value_ev5 | 2656 | 40.8 | 41.1 | $-1140.42 | -4.3% | $-140.42 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 3048 | 49.3 | 49.3 | $-1432.67 | -4.7% | $-432.67 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3048 | 50.7 | 51.0 | $-1593.08 | -5.2% | $-593.08 | -3.0 | done | losing for real |
| trend_filter | 2156 | 48.6 | 50.3 | $-1867.18 | -8.7% | $-867.18 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3628 | 49.2 | 50.2 | $-2184.77 | -6.0% | $-1184.77 | -3.7 | done | losing for real |
| coinflip | 5220 | 50.0 | 50.0 | $-2202.00 | -4.2% | $-1202.00 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5220 | 50.1 | 51.3 | $-3235.37 | -6.2% | $-2235.37 | -4.6 | done | losing for real |
| always_up | 5220 | 48.0 | 49.3 | $-3556.15 | -6.8% | $-2556.15 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9156 | 48.1 | 48.8 | $-4774.90 |
| ETH | 9845 | 48.1 | 48.0 | $-5048.98 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
