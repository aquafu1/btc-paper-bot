# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 932 windows, 25755 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1165 | 38.0 | 39.1 | $-672.90 | -5.8% | $327.10 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2631 | 51.0 | 50.6 | $-878.60 | -3.3% | $121.40 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2197 | 50.1 | 49.8 | $-945.41 | -4.3% | $54.59 | -2.0 | done | losing for real |
| trend_filter | 1529 | 49.9 | 51.0 | $-1068.27 | -7.0% | $-68.27 | -2.8 | done | losing for real |
| value_ev5 | 1770 | 39.7 | 41.0 | $-1117.33 | -6.3% | $-117.33 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2197 | 49.9 | 50.9 | $-1517.97 | -6.9% | $-517.97 | -3.3 | done | losing for real |
| coinflip | 3720 | 50.4 | 50.4 | $-1575.80 | -4.2% | $-575.80 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2631 | 49.0 | 50.2 | $-1687.33 | -6.4% | $-687.33 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3720 | 50.9 | 51.6 | $-1910.50 | -5.1% | $-910.50 | -3.2 | done | losing for real |
| always_up | 3720 | 46.8 | 49.7 | $-3813.60 | -10.3% | $-2813.60 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5869 | 48.1 | 49.1 | $-3445.27 |
| ETH | 6405 | 48.2 | 48.6 | $-4033.34 |
| SOL | 6720 | 48.1 | 48.6 | $-3984.99 |
| XRP | 6761 | 48.3 | 48.5 | $-3869.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
