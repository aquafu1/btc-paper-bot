# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 393 windows, 10761 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sun 12:15 AM | too few trades (196/200) |
| value_ev10 | 512 | 40.6 | 40.5 | $-145.67 | -2.8% | $854.33 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 913 | 50.6 | 49.8 | $-216.55 | -2.4% | $783.45 | -0.7 | done | can't tell from luck |
| value_ev5 | 759 | 42.2 | 42.2 | $-261.20 | -3.4% | $738.80 | -0.8 | done | can't tell from luck |
| trend_filter | 610 | 49.5 | 50.5 | $-358.76 | -5.9% | $641.24 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1083 | 49.1 | 49.7 | $-506.57 | -4.7% | $493.43 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1083 | 50.9 | 52.1 | $-655.20 | -6.0% | $344.80 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 913 | 49.4 | 52.2 | $-810.27 | -8.9% | $189.73 | -2.8 | done | losing for real |
| coinflip | 1564 | 49.7 | 50.8 | $-874.44 | -5.6% | $125.56 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1564 | 49.7 | 51.5 | $-1085.31 | -6.9% | $-85.31 | -2.8 | done | losing for real |
| always_up | 1564 | 46.3 | 50.7 | $-1883.41 | -12.0% | $-883.41 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2435 | 47.7 | 49.4 | $-1684.74 |
| ETH | 2706 | 47.9 | 48.9 | $-1679.56 |
| SOL | 2784 | 47.9 | 49.5 | $-2069.67 |
| XRP | 2836 | 48.9 | 49.2 | $-1390.38 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
