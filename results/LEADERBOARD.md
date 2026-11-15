# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 400 windows, 10950 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 12:30 AM | too few trades (199/200) |
| value_ev10 | 518 | 40.5 | 40.5 | $-164.41 | -3.2% | $835.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 930 | 50.6 | 49.8 | $-217.27 | -2.3% | $782.73 | -0.7 | done | can't tell from luck |
| value_ev5 | 774 | 42.2 | 42.2 | $-257.60 | -3.3% | $742.40 | -0.8 | done | can't tell from luck |
| trend_filter | 621 | 49.9 | 50.6 | $-323.33 | -5.2% | $676.67 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1101 | 49.4 | 49.8 | $-458.91 | -4.2% | $541.09 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1101 | 50.6 | 52.1 | $-723.79 | -6.6% | $276.21 | -2.3 | done | losing for real |
| coinflip | 1592 | 50.0 | 50.9 | $-814.81 | -5.1% | $185.19 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 930 | 49.4 | 52.1 | $-834.41 | -9.0% | $165.59 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1592 | 49.9 | 51.6 | $-1061.96 | -6.7% | $-61.96 | -2.8 | done | losing for real |
| always_up | 1592 | 46.1 | 50.8 | $-1997.06 | -12.5% | $-997.06 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2473 | 47.8 | 49.5 | $-1698.13 |
| ETH | 2752 | 48.0 | 48.9 | $-1657.43 |
| SOL | 2834 | 48.0 | 49.5 | $-2092.77 |
| XRP | 2891 | 48.9 | 49.3 | $-1462.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
