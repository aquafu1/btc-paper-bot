# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 9:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 391 windows, 10717 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sun 12:00 AM | too few trades (196/200) |
| value_ev10 | 510 | 40.4 | 40.5 | $-169.03 | -3.3% | $830.97 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 908 | 50.8 | 49.7 | $-187.92 | -2.1% | $812.08 | -0.6 | done | can't tell from luck |
| value_ev5 | 756 | 41.9 | 42.2 | $-295.47 | -3.9% | $704.53 | -0.9 | done | can't tell from luck |
| trend_filter | 606 | 49.8 | 50.5 | $-318.76 | -5.3% | $681.24 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1078 | 49.4 | 49.7 | $-456.57 | -4.2% | $543.43 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1078 | 50.6 | 52.1 | $-711.32 | -6.6% | $288.68 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 908 | 49.2 | 52.2 | $-845.03 | -9.3% | $154.97 | -2.9 | done | losing for real |
| coinflip | 1559 | 49.8 | 50.8 | $-867.37 | -5.6% | $132.63 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1559 | 49.8 | 51.5 | $-1035.31 | -6.6% | $-35.31 | -2.7 | done | losing for real |
| always_up | 1559 | 46.4 | 50.7 | $-1854.78 | -11.9% | $-854.78 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2419 | 47.7 | 49.4 | $-1651.59 |
| ETH | 2696 | 48.0 | 48.9 | $-1663.23 |
| SOL | 2776 | 47.9 | 49.5 | $-2051.13 |
| XRP | 2826 | 48.9 | 49.2 | $-1402.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
